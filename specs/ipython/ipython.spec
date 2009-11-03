# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Enhanced interactive Python shell
Name: ipython
Version: 0.7.1.fix1
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://ipython.scipy.org/

Source: http://ipython.scipy.org/dist/ipython-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python, python-devel

%description
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}"

%{__install} -Dp -m0644 doc/ipython.1.gz %{buildroot}%{_mandir}/man1/ipython.1.gz
%{__install} -Dp -m0644 doc/pycolor.1.gz %{buildroot}%{_mandir}/man1/pycolor.1.gz
%{__install} -Dp -m0644 doc/ipython.el %{buildroot}%{_datadir}/emacs/site-lisp/ipython.el

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/ChangeLog doc/COPYING doc/NEWS doc/README.txt doc/*.txt doc/examples/ doc/manual/
%doc %{_mandir}/man1/ipython.1*
%doc %{_mandir}/man1/pycolor.1*
%{_bindir}/ipython
%{_bindir}/pycolor
%{python_sitelib}/IPython/

%changelog
* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.7.1.fix1-1
- Initial package. (using DAR)
