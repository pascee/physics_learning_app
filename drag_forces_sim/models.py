from django.db import models

class Drag_Object(models.Model):
    #defining all of the fields
    obj_name = models.CharField(max_length = 200)
    drag_coeficient = models.DecimalField(max_digits=10, decimal_places=3)
    current_speed = models.DecimalField(max_digits=13, decimal_places=3)
    gravitational_constant = models.DecimalField(max_digits=5, decimal_places=2)
    obj_mass = models.DecimalField(max_digits=15, decimal_places=3)

    #returns the name of the object
    def __str__(self):
        return self.obj_name
    
    # finds the instantaneous drag force, used in instances in which the object
    # is small and falling through a liquid 
    def return_drag_force_v(self):
        d_force = self.current_speed * self.drag_coeficient * -1
        return d_force
    
    # finds the instantaneous drag force, used in instances in which the object
    # is larger and falling through the air
    def return_drag_force_v_squared(self):
        d_force = self.current_speed * self.current_speed * self.drag_coeficient * -1
        return d_force

    # returns the force due to gravity
    # down is negative, but the gravitational constant is positive, so it is
    # multiplied by -1.
    def return_gravitational_force(self):
        g_force = self.gravitational_constant * self.obj_mass * -1
        return g_force
    
    # returns the total force, taking a boolean to determine which drag formula
    # is used.
    def return_total_force(self, v_squared):
        if(v_squared):
            return (self.return_gravitational_force() + self.return_drag_force_v_squared())
        else:
            return (self.return_gravitational_force() + self.return_drag_force_v())
        
    #returns the total acceleration of the object
    def return_total_acceleration(self, v_squared):
        if(v_squared):
            return (self.return_total_force(True) / self.obj_mass)
        else:
            return(self.return_total_force(False) / self.obj_mass)
