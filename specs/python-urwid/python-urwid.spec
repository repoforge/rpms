# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name urwid

Summary: Console UI Library for Python
Name: python-urwid
Version: 0.9.5
Release: 2
License: LGPL
Group: Development/Libraries
URL: http://excess.org/urwid/

Source: http://excess.org/urwid/urwid-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.1
Requires: python >= 2.1

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc reference.html tutorial.html
%{python_sitelib}/urwid/
%ghost %{python_sitelib}/urwid/*.pyo

%changelog
* Mon Aug 07 2006 Dag Wieers <dag@wieers.com> - 0.9.5-2
- Removed the erroneous python-curses dependency.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Initial package. (using DAR)
