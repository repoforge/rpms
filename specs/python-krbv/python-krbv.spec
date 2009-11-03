# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name python-krbV

Summary: Python extension module for Kerberos 5
Name: python-krbv
Version: 1.0.13
Release: 2%{?dist}
License: LGPL
Group: Development/Languages
URL: http://people.redhat.com/mikeb/python-krbV/

Source: http://people.redhat.com/mikeb/python-krbV/python-krbV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.2
BuildRequires: krb5-devel >= 1.2.2

Obsoletes: python-krbV <= %{version}-%{release}
provides: python-krbV = %{version}-%{release}

%description
python-krbV allows python programs to use Kerberos 5 authentication/security.

%prep
%setup -n %{real_name}-%{version}

%build
export LIBNAME="%{_lib}"
export CFLAGS="%{optflags}"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README krbV-code-snippets.py
%{python_sitearch}/krbVmodule.so
%exclude %{python_sitearch}/krbVmodule.la

%changelog
* Tue Oct 16 2007 Dag Wieers <dag@wieers.com> - 1.0.13-2
- Added AUTHORS, ChangeLog and NEWS.

* Mon Oct 15 2007 Dag Wieers <dag@wieers.com> - 1.0.13-1
- Initial package. (using DAR)
