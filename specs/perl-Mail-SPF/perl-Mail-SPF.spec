# $Id$
# Authority: dag
# Upstream: Julian Mehnle <julian$mehnle,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-SPF
%define real_version 2.004000

Summary: Perl module that implements Sender Policy Framework
Name: perl-Mail-SPF
Version: 2.004
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-SPF/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-SPF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker), perl(Module::Build)

%description
Mail-SPF is a Perl module that implements Sender Policy Framework.

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
%doc CHANGES INSTALL LICENSE MANIFEST META.yml README SIGNATURE TODO
%{_mandir}/man1/spfquery.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/spfquery
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/SPF/
%{perl_vendorlib}/Mail/SPF.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 2.004-1
- Initial package. (using DAR)
