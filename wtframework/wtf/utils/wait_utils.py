##########################################################################
#This file is part of WTFramework. 
#
#    WTFramework is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    WTFramework is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with WTFramework.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################

from datetime import datetime, timedelta
from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
import time


class OperationTimeoutError(Exception):
    """
    Timeout Error
    This error is thrown when a wait function times out.
    """
    pass

def wait_until(condition, timeout=WTF_TIMEOUT_MANAGER.NORMAL, sleep=0.5, pass_exceptions=False):
    '''
    Waits until URL matches the expression.
    @param condition: Lambda expression to wait on.  Lambda expression 
    should return true when conditions is met.
    @type condition: lambda
    @param timeout: Timeout period in seconds.
    @rtype: int
    '''
    end_time = datetime.now() + timedelta(seconds = timeout)
    while datetime.now() < end_time:
        try:
            if condition():
                return
        except Exception as e:
            if pass_exceptions:
                raise e
            else:
                pass
        time.sleep(sleep)

    raise OperationTimeoutError("Operation timed out.")

