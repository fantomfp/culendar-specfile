%{?!python3_pkgversion:%global python3_pkgversion 3}


Name:           culendar
Version:        0.20251111^20261026git6b903a2d
Release:        1%{?dist}
Summary:        Culendar is a CUrses CaLENDAR: CLI Agenda in Python
License:        WTFPL
URL:            https://framagit.org/mit/culendar
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
Culendar is a free/libre calendar application in python and
curses.

Displays your events on a week, hour by hour
Displays a TODO list
Adds, deletes, edits, categorizes events
Colour themes for your categorized events
Imports from ICalendar format or from calcurse
files
Customizable
Displays webcals
Deals with caldavs



%prep
%autosetup -p1 -n %{name}


%build
%py3_build


%install
%py3_install



%files
%license LICENSE
%doc README.md
# For noarch packages: sitelib
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/



%changelog
%autochangelog
