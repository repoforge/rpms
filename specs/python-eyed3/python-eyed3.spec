# $Id$
# Authority: dag
# Upstream: Travis Shirk <travis@pobox.com>, Ryan Finnie <ryan@finnie.org>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name eyeD3

Summary: Python Module for ID3 Tag Manipulation
Name: python-eyed3
Version: 0.6.14
Release: 1
License: GPL
Group: Development/Libraries
URL: http://eyed3.nicfit.net/

Source: http://eyed3.nicfit.net/releases/eyeD3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python, python-devel
Obsoletes: python-eyeD3 <= %{version}

%description
python-eyed3 is a python module for the manipulation of ID3 tags.
It supports versions 1.0, 1.1, 2.3, and 2.4 of the ID3 standard.
It can also retrieve information, such as length and bit rate,
from an MP3 file.

%prep
%setup -n %{real_name}-%{version}

%build
export CFLAGS="%{optflags}"
%configure
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%{__install} -Dp -m755 bin/eyeD3 %{buildroot}%{_bindir}/eyeD3

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO
%{_bindir}/eyeD3
%{python_sitelib}/eyeD3/

%changelog
* Thu May 10 2007 Dag Wieers <dag@wieers.com> - 0.6.14-1
- Updated to release 0.6.14.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.6.13-1
- Updated to release 0.6.13.

* Mon Feb 19 2007 Dag Wieers <dag@wieers.com> - 0.6.12-1
- Updated to release 0.6.12.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Initial package. (using DAR)
