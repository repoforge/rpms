# $Id: armagetron.spec 173 2004-03-28 04:37:02Z dag $
# Authority: matthias

# Dist: nodist

%define prefix %{_prefix}/games/armagetron

Summary: Sounds and graphics to give armagetron the real 'Tron' look
Name: armagetron-moviepack
Version: 1.0
Release: 1
License: Proprietary
Group: Amusements/Games
Source0: http://armagetron.sourceforge.net/addons/moviepack.zip
Source1: http://armagetron.sourceforge.net/addons/moviesounds_mq.zip
Source2: settings.cfg.realistic
URL: http://armagetron.sourceforge.net/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: armagetron

%description
This package includes all files needed by armagetron to have the "real" look
from the original Tron movie. This includes neat colorful graphics and a few
sounds.
In this package's documentation directory, you will also find a new config
file that you can use in %{_sysconfdir}/armagetron to have the game be a bit
more realistic (read "fast!" ;-)).


%prep
# Create the directory, but don't unpack anything
%setup -c -T


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{prefix}
# The main moviepack stuff
unzip -d %{buildroot}%{prefix}/ %{SOURCE0}
unzip -d %{buildroot}%{prefix}/ %{SOURCE1}

# The 'realistic' settings
%{__cp} %{SOURCE2} settings.cfg.realistic


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%doc settings.cfg.realistic
%{prefix}/moviepack
%{prefix}/moviesounds


%changelog
* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 1.0-1
- Split off the moviepack files in order to not have them rebuilt and
  transferred each time a new armagetron comes out and have it noarch.

