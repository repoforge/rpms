# $Id$
# Authority: dries

Summary: SRCP server for model railways
Name: srcpd
Version: 2.0.10
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://srcpd.sourceforge.net/

Source: http://dl.sf.net/srcpd/srcpd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel

%description
SRCP is an comminication protocol designed to integrate all model railroad 
systems. Further key features are full multiuser capabilities and simplified 
user interface development.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man8/srcpd*
%{_sbindir}/srcpd
%config(noreplace) %{_sysconfdir}/srcpd.conf

%changelog
* Sun Dec 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.10-1
- Initial package.
