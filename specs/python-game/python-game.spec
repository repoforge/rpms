# $Id$
# Authority: dag

%define real_name pygame

Summary: Python module for interfacing with the SDL multimedia library
Name: python-game
Version: 1.6
Release: 0
License: LGPL style
Group: Development/Libraries
URL: http://pygame.seul.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://pygame.seul.org/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: python-numeric, smpeg-devel,
BuildRequires: SDL_mixer-devel, SDL_image-devel, SDL_ttf-devel
Requires: SDL >= 1.2.2

Obsoletes: pygame
Provides: pygame

%description
pygame is a Python wrapper module for the SDL multimedia library, written by
Pete Shinners.  It contains python functions and classes that will allow you to
use SDL's support for playing cdroms, audio and video output, and keyboard,
mouse and joystick input. pygame also includes support for the Numerical Python
extension. pygame is the successor to the pySDL wrapper project, written by
Mark Baker.

%package doc
Summary: Pygame documentation and example programs
Group: Documentation

%description doc
pygame is a Python wrapper module for the SDL multimedia library, written by
Pete Shinners.  It contains python functions and classes that will allow you to
use SDL's support for playing cdroms, audio and video output, and keyboard,
mouse and joystick input. pygame also includes support for Numerical Python
extension. pygame is the successor to the pySDL wrapper project, written by
Mark Baker.

Install pygame-doc if you need the API documentation and example programs.

%prep
%setup -n %{real_name}-%{version}

%build
python config.py
python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--prefix="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc WHATSNEW readme.*
%{_libdir}/python*/site-packages/pygame/
%{_includedir}/python*/pygame/

%files doc
%defattr(-, root, root, 0755)
%doc docs/ examples/

%changelog
* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Updated to release 1.6.

* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 1.5.6-0
- Initial package. (using DAR)
