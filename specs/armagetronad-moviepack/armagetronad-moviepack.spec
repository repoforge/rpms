# $Id$
# Authority: matthias
# Dist: nodist

%define prefix %{_prefix}/games/armagetronad

Summary: Sounds and graphics to give armagetronad the real 'Tron' look
Name: armagetronad-moviepack
Version: 1.0
Release: 2
License: Proprietary
Group: Amusements/Games
URL: http://armagetronad.sourceforge.net/
Source0: http://armagetron.sourceforge.net/addons/moviepack.zip
Source1: http://armagetron.sourceforge.net/addons/moviesounds_mq.zip
Source2: settings.cfg.realistic
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: armagetronad
Obsoletes: armagetron-moviepack <= 1.0-1
Provides: armagetron-moviepack = %{version}-%{release}

%description
This package includes all files needed by armagetronad to have the "real" look
from the original Tron movie. This includes neat colorful graphics and a few
sounds.
In this package's documentation directory, you will also find a new config
file that you can use in %{_sysconfdir}/armagetronad to have the game be a bit
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
%{prefix}/moviepack/
%{prefix}/moviesounds/


%changelog
* Mon Mar 14 2005 Matthias Saou <http://freshrpms.net/> 1.0-2
- Initial RPM release based on my armagetron-moviepack package.

