from django.db import models

class DragObject(models.Model):
    #defining all of the fields
    objName = models.CharField(max_length = 200)
    dragCoeficient = models.DecimalField(max_digits=10, decimal_places=3)
    currentSpeed = models.DecimalField(max_digits=13, decimal_places=3)
    gravitationalConstant = models.DecimalField(max_digits=5, decimal_places=2)
    objMass = models.DecimalField(max_digits=15, decimal_places=3)

    #returns the name of the object
    def __str__(self):
        return self.objName
    
    # finds the instantaneous drag force, used in instances in which the object
    # is small and falling through a liquid 
    def returnDragForceV(self):
        d_force = self.currentSpeed * self.dragCoeficient * -1
        return d_force
    
    # finds the instantaneous drag force, used in instances in which the object
    # is larger and falling through the air
    def returnDragForceVSquared(self):
        d_force = self.currentSpeed * self.currentSpeed * self.dragCoeficient * -1
        return d_force

    # returns the force due to gravity
    # down is negative, but the gravitational constant is positive, so it is
    # multiplied by -1.
    def returnGravitationalForce(self):
        g_force = self.gravitationalConstant * self.objMass * -1
        return g_force
    
    # returns the total force, taking a boolean to determine which drag formula
    # is used.
    def returnTotalForce(self, VSquared):
        if(VSquared):
            return (self.returnGravitationalForce() + self.returnDragForceVSquared())
        else:
            return (self.returnGravitationalForce() + self.returnDragForceV())
        
    #returns the total acceleration of the object
    def returnTotalAcceleration(self, VSquared):
        if(VSquared):
            return (self.returnTotalForce(True) / self.objMass)
        else:
            return(self.returnTotalForce(False) / self.objMass)
