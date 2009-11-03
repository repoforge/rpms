# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan@ali.as>, L<http://ali.as/>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-BadExample

Summary: Perl document, yes. Perl code, no damn way!
Name: perl-Acme-BadExample
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-BadExample/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Acme-BadExample-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005 
BuildRequires: perl(File::Spec) >= 0.8
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005 
AutoReqProv: no

%description
Perl document, yes. Perl code, no damn way!

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Acme::BadExample.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/BadExample.pm

%changelog
* Wed Jul  8 2009 Christoph Maser <cmr@financial.com> - 1.01-1
- Updated to version 1.01.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
