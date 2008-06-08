# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name urwid

Summary: Console UI Library for Python
Name: python-urwid
Version: 0.9.8.2
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://excess.org/urwid/

Source: http://excess.org/urwid/urwid-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.1
Requires: python >= 2.1
Obsoletes: urwid < %{version}-%{release}
Provides: urwid = %{version}-%{release}

%description
Urwid is a Python library for making text console applications. It has
many features including fluid interface resizing, support for UTF-8 and CJK
encodings, standard and custom text layout modes, simple markup for setting
text attributes, and a powerful, dynamic list box that handles a mix of
widget types. It is flexible, modular, and leaves the developer in control.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%{__install} -d -m0755 examples/
%{__install} -p -m0755 {browse,calc,dialog,edit,fib,graph,tour}.py examples/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc reference.html tutorial.html examples/
%{python_sitelib}/urwid/
%ghost %{python_sitelib}/urwid/*.pyo

%changelog
* Fri Jun 06 2008 Dag Wieers <dag@wieers.com> - 0.9.8.2-1
- Updated to release 0.9.8.2.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Mon Aug 07 2006 Dag Wieers <dag@wieers.com> - 0.9.5-2
- Removed the erroneous python-curses dependency.
- Added urwid examples.
- Added urwid obsoletes and provides.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Initial package. (using DAR)
