# $Id$
# Authority: dag
# Upstream: Benjamin Pannier <karo$artcom,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jail

Summary: Perl module for grabbing video, modifying images and display images
Name: perl-Jail
Version: 0.8
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jail/

Source: http://www.cpan.org/authors/id/B/BP/BPANNIER/Jail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Jail is a Perl module for grabbing video, modifying images
and display images.

This package contains the following Perl module:

    Jail

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
%doc Changes MANIFEST
%doc %{_mandir}/man3/Jail.3pm*
%{perl_vendorarch}/Jail.pm
%{perl_vendorarch}/auto/Jail/

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
