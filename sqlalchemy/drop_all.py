#!/usr/bin/env python

import arrow
import yaml
from sqlalchemy import and_, or_

from crud import Session, create_database, drop_database, recreate_database

drop_database()
