# $Id$
# Authority: dag
# Upstream: DJ Adams <dj,adams$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jabber-Connection

Summary: Perl module that provides simple connectivity functions for Jabber
Name: perl-Jabber-Connection
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jabber-Connection/

Source: http://www.cpan.org/modules/by-module/Jabber/Jabber-Connection-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Jabber-Connection is a Perl module that provides simple connectivity
functions for Jabber.

This package contains the following Perl module:

    Jabber::Connection

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man3/Jabber::Connection.3pm*
%doc %{_mandir}/man3/Jabber::NS.3pm*
%doc %{_mandir}/man3/Jabber::NodeFactory.3pm*
%dir %{perl_vendorlib}/Jabber/
%{perl_vendorlib}/Jabber/Connection.pm
%{perl_vendorlib}/Jabber/NS.pm
%{perl_vendorlib}/Jabber/NodeFactory.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
