# $Id: _template.spec 765 2004-05-20 17:33:53Z dag $
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

Summary: RPM macros used by the RPMForge project
Name: rpm-macros-rpmforge
Version: 0
Release: 1
License: GPL
Group: Development/Tools
URL: http://rpmforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
RPM macros used by the RPMForge project.

%prep

%{__cat} <<EOF >macros.rpmforge
%if %{?dist:1}0
### Current distribution
%%dist %dist
%%%dist 1
%else
### Current disitribution undefine in original buildsystem
#%%define dist ???
#%%define ??? 1
%endif

%if "%dist" == "fc1"
### Fedora Core 1
%%errata 100
%%_without_alsa 1
%%_without_theora 1
%endif
%if "%dist" == "el3"
### Red Hat Enterprise Linux 3
%%errata 91
%%_without_alsa 1
%%_without_fribidi 1
%%_without_theora 1
%endif
%if "%dist" == "rh9"
### Red Hat Linux 9
%%errata 90
%%_without_alsa 1
%%_without_fribidi 1
%%_without_theora 1
%endif
%if "%dist" == "rh8"
### Red Hat Linux 8.0
%%errata 80
%%_without_alsa 1
%%_without_fribidi 1
%%_without_theora 1
%endif
%if "%dist" == "rh7"
### Red Hat Linux 7.3
%%errata 73
%%_without_alsa 1
%%_without_freedesktop 1
%%_without_fribidi 1
%%_without_gnomevfs2 1
%%_without_theora 1
%endif
%if "%dist" == "el2"
### Red hat Enterprise Linux 2.1
%%errata 72
%%_without_alsa 1
%%_without_freedesktop 1
%%_without_fribidi 1
%%_without_gnomevfs2 1
%%_without_theora 1
%endif
%if "%dist" == "rh6"
### Red Hat Linux 6.2
%%errata 62
%%_without_alsa 1
%%_without_freedesktop 1
%%_without_fribidi 1
%%_without_gnomevfs2 1
%%_without_theora 1
%endif
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0644 macros.rpmforge %{buildroot}%{_sysconfdir}/rpm/macros.rpmforge

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/rpm/macros.rpmforge

%changelog
* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 0-1
- Initial package. (using DAR)
