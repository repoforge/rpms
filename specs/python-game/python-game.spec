# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pygame

Summary: Python module for interfacing with the SDL multimedia library
Name: python-game
Version: 1.8.1
Release: 1%{?dist}
License: LGPL style
Group: Development/Libraries
URL: http://pygame.org/

Source: http://www.pygame.org/ftp/%{real_name}-%{version}release.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-numeric, smpeg-devel, python-devel
BuildRequires: SDL_mixer-devel, SDL_image-devel, SDL_ttf-devel
Requires: SDL >= 1.2.2

Obsoletes: pygame <= %{version}-%{release}
Provides: pygame = %{version}-%{release}

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
%setup -n %{real_name}-%{version}release

%build
%{__python} config.py
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt WHATSNEW
%{python_sitearch}/pygame/
%{_includedir}/python*/pygame/

%files doc
%defattr(-, root, root, 0755)
%doc docs/ examples/

%changelog
* Fri Aug 01 2008 Dag Wieers <dag@wieers.com> - 1.8.1-1
- Updated to release 1.8.1.

* Tue Apr 08 2008 Dag Wieers <dag@wieers.com> - 1.8.0-1
- Updated to release 1.8.0.

* Wed Aug 17 2005 C.Lee Taylor <leet@leenx.co.za> - 1.7.1-0
- Updated to release 1.7.1.
- Fix URL for new site.

* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Updated to release 1.6.

* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 1.5.6-0
- Initial package. (using DAR)
