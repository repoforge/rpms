# $Id$
# Authority: dfateyev
# Upstream: Rocky Bernstein <rocky$gnu,org>

# ExcludeDist: el2 el3 el4

%bcond_with tests
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Name: pydb
Summary: Pydb is an expanded version of the Python debugger
Version: 1.26
Release: 1%{?dist}
License: GPLv2+
Group: Development/Debuggers
URL: http://bashdb.sourceforge.net/pydb/

Source: http:/downloads.sourceforge.net/project/bashdb/%{name}/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3.4
Requires: python

%if !%{?el5:1}0
# rhel5 emacs (21) is too outdated
%package -n emacs-pydb
Summary: Pydb support for Emacs
Group: Development/Debuggers
BuildRequires: emacs emacs-common emacs-el >= 21
Requires: pydb = %{version}-%{release}
Requires: emacs >= 21

%description -n emacs-pydb
Pydb support for Emacs.
%endif

%description
pydb is an expanded version of the Python debugger loosely based on
the gdb command set. It also has all of the features found in an
earlier version of pydb.py that was distributed with the debugger
GUI ddd.

%prep
%setup -n %{name}-%{version}

%build
%configure --with-site-packages=%{python_sitelib} --with-lispdir=%{_datadir}/emacs/site-lisp
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL="install -p" DESTDIR=%{buildroot}
%{__rm} -f "%{buildroot}%{_infodir}/dir"
cd %{buildroot}%{_bindir}
%{__rm} -f pydb
%{__ln_s} -f %{python_sitelib}/pydb/pydb.py pydb

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_bindir}/*
%{python_sitelib}/pydb
%{_mandir}/man1/*

%if !%{?el5:1}0
%files -n emacs-pydb
%defattr(-,root,root,-)
%{_datadir}/emacs/site-lisp/pydb.el*
%endif

%changelog
* Sun Apr 8 2012 Denis Fateyev <denis@fateyev.com> - 1.26-1
- Initial package.
