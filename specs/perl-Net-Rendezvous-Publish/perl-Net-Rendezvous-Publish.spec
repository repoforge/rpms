# $Id$
# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Rendezvous-Publish

Summary: Publish Rendezvous services
Name: perl-Net-Rendezvous-Publish
Version: 0.04
Release: 2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Rendezvous-Publish/

Source: http://www.cpan.org/modules/by-module/Net/Net-Rendezvous-Publish-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Class::Accessor::Lvalue)

%description
With this module, you can publish Rendezvous services.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/Net::Rendezvous::Publish*
%{perl_vendorlib}/Net/Rendezvous/Publish.pm
%{perl_vendorlib}/Net/Rendezvous/Publish/
%dir %{perl_vendorlib}/Net/Rendezvous/

%changelog
* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 0.04-2
- perl(Class::Accessor::Lvalue) req added, thanks to Earl Chew.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.01
- Initial package.
