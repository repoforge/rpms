# $Id: $

# Authority: dries
# Upstream: Douglas Hanks

Summary: sudo shell
Name: sudosh
Version: 1.3.4
Release: 1
License: Open Software License
Group: Applications/System
URL: http://sourceforge.net/projects/sudosh

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

#Source: http://dl.sf.net/sudosh/sudosh-%{version}.tar.gz
Source: http://sudosh.sourceforge.net/sudosh-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: sudo

%description
sudosh works directly with sudo to provide a fully functional shell that
users may use to obtain full root access. Unlike providing a team of system
administrators full root access through sudo, it guarantees that detailed
logs are kept. It uses the script command in conjunction with a secure FIFO
and comes with a utility to view sessions and drill down deeper and see the
actual session output. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc NEWS README AUTHORS COPYING INSTALL
%{_bindir}/*

%changelog
* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> - 1.3.4-1
- Update to release 1.3.4.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Update to release 1.3.2.

* Mon Oct 18 2004 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1
- Update to release 1.2.2.

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Initial package.
