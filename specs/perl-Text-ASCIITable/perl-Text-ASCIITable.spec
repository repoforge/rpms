# $Id$
# Authority: dag
# Upstream: Håkon Nessjøen <lunatic$_NOSPAM_skonux,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-ASCIITable

Summary: Perl module to create a nice formatted table using ASCII characters
Name: perl-Text-ASCIITable
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-ASCIITable/

Source: http://www.cpan.org/modules/by-module/Text/Text-ASCIITable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
perl-Text-ASCIITable is a Perl module to create a nice formatted table
using ASCII characters.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
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
%doc %{_mandir}/man3/Text::ASCIITable.3pm*
%doc %{_mandir}/man3/Text::ASCIITable::Wrap.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/ASCIITable/
%{perl_vendorlib}/Text/ASCIITable.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
