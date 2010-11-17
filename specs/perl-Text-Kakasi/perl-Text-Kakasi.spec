# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

### EL2 ships with perl-Text-Kakasi-1.04-4
%{?el2:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Kakasi

Summary: Perl module implements a frontend to kakasi
Name: perl-Text-Kakasi
Version: 2.04
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Kakasi/

Source: http://www.cpan.org/modules/by-module/Text/Text-Kakasi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: kakasi-devel

%description
perl-Text-Kakasi is a Perl module implements a frontend to kakasi.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog.1 Changes MANIFEST META.yml README README.jp
%doc %{_mandir}/man3/Text::Kakasi.3pm*
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/Kakasi.pm
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/Kakasi/

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 2.04-1
- Initial package. (using DAR)
