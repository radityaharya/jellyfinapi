# -*- coding: utf-8 -*-


class SessionMessageTypeEnum(object):

    """Implementation of the 'SessionMessageType' enum.

    The different kinds of messages that are used in the WebSocket api.

    Attributes:
        FORCEKEEPALIVE: TODO: type description here.
        GENERALCOMMAND: TODO: type description here.
        USERDATACHANGED: TODO: type description here.
        SESSIONS: TODO: type description here.
        PLAY: TODO: type description here.
        SYNCPLAYCOMMAND: TODO: type description here.
        SYNCPLAYGROUPUPDATE: TODO: type description here.
        PLAYSTATE: TODO: type description here.
        RESTARTREQUIRED: TODO: type description here.
        SERVERSHUTTINGDOWN: TODO: type description here.
        SERVERRESTARTING: TODO: type description here.
        LIBRARYCHANGED: TODO: type description here.
        USERDELETED: TODO: type description here.
        USERUPDATED: TODO: type description here.
        SERIESTIMERCREATED: TODO: type description here.
        TIMERCREATED: TODO: type description here.
        SERIESTIMERCANCELLED: TODO: type description here.
        TIMERCANCELLED: TODO: type description here.
        REFRESHPROGRESS: TODO: type description here.
        SCHEDULEDTASKENDED: TODO: type description here.
        PACKAGEINSTALLATIONCANCELLED: TODO: type description here.
        PACKAGEINSTALLATIONFAILED: TODO: type description here.
        PACKAGEINSTALLATIONCOMPLETED: TODO: type description here.
        PACKAGEINSTALLING: TODO: type description here.
        PACKAGEUNINSTALLED: TODO: type description here.
        ACTIVITYLOGENTRY: TODO: type description here.
        SCHEDULEDTASKSINFO: TODO: type description here.
        ACTIVITYLOGENTRYSTART: TODO: type description here.
        ACTIVITYLOGENTRYSTOP: TODO: type description here.
        SESSIONSSTART: TODO: type description here.
        SESSIONSSTOP: TODO: type description here.
        SCHEDULEDTASKSINFOSTART: TODO: type description here.
        SCHEDULEDTASKSINFOSTOP: TODO: type description here.
        KEEPALIVE: TODO: type description here.

    """

    FORCEKEEPALIVE = "ForceKeepAlive"

    GENERALCOMMAND = "GeneralCommand"

    USERDATACHANGED = "UserDataChanged"

    SESSIONS = "Sessions"

    PLAY = "Play"

    SYNCPLAYCOMMAND = "SyncPlayCommand"

    SYNCPLAYGROUPUPDATE = "SyncPlayGroupUpdate"

    PLAYSTATE = "Playstate"

    RESTARTREQUIRED = "RestartRequired"

    SERVERSHUTTINGDOWN = "ServerShuttingDown"

    SERVERRESTARTING = "ServerRestarting"

    LIBRARYCHANGED = "LibraryChanged"

    USERDELETED = "UserDeleted"

    USERUPDATED = "UserUpdated"

    SERIESTIMERCREATED = "SeriesTimerCreated"

    TIMERCREATED = "TimerCreated"

    SERIESTIMERCANCELLED = "SeriesTimerCancelled"

    TIMERCANCELLED = "TimerCancelled"

    REFRESHPROGRESS = "RefreshProgress"

    SCHEDULEDTASKENDED = "ScheduledTaskEnded"

    PACKAGEINSTALLATIONCANCELLED = "PackageInstallationCancelled"

    PACKAGEINSTALLATIONFAILED = "PackageInstallationFailed"

    PACKAGEINSTALLATIONCOMPLETED = "PackageInstallationCompleted"

    PACKAGEINSTALLING = "PackageInstalling"

    PACKAGEUNINSTALLED = "PackageUninstalled"

    ACTIVITYLOGENTRY = "ActivityLogEntry"

    SCHEDULEDTASKSINFO = "ScheduledTasksInfo"

    ACTIVITYLOGENTRYSTART = "ActivityLogEntryStart"

    ACTIVITYLOGENTRYSTOP = "ActivityLogEntryStop"

    SESSIONSSTART = "SessionsStart"

    SESSIONSSTOP = "SessionsStop"

    SCHEDULEDTASKSINFOSTART = "ScheduledTasksInfoStart"

    SCHEDULEDTASKSINFOSTOP = "ScheduledTasksInfoStop"

    KEEPALIVE = "KeepAlive"
