# $Id$
# Authority: dag
# Upstream: Sue Spence <sue_cpan$pennine,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kwiki-Attachments

Summary: Kwiki Page Attachments plugin
Name: perl-Kwiki-Attachments
Version: 0.21
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Kwiki-Attachments/

Source: http://www.cpan.org/modules/by-module/Kwiki/Kwiki-Attachments-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Kwiki)

%description
Kwiki Page Attachments plugin.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Kwiki::Attachments.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Kwiki/
#%{perl_vendorlib}/Kwiki/Attachments/
%{perl_vendorlib}/Kwiki/Attachments.pm

%changelog
* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Updated to version 0.21.

* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
