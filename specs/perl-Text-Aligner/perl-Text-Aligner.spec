# $Id$
# Authority: dag
# Upstream: Anno Siegel <siegel$zrz,tu-berlin,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Aligner

Summary: Used to justify strings to various alignment styles
Name: perl-Text-Aligner
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Aligner/

Source: http://www.cpan.org/modules/by-module/Text/Text-Aligner-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Used to justify strings to various alignment styles.

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Text::Aligner.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Aligner/
%{perl_vendorlib}/Text/Aligner.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
