# $Id$
# Authority: dag
# Upstream: Domenico Delle Side <dds$gnulinux,it>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-CHM

Summary: Perl module for handling MS Compiled HtmlHelp files
Name: perl-Text-CHM
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-CHM/

Source: http://www.cpan.org/modules/by-module/Text/Text-CHM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: chmlib-devel

%description
perl-Text-CHM is a Perl module for handling MS Compiled HtmlHelp files.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Text::CHM.3pm*
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/CHM.pm
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/CHM/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
