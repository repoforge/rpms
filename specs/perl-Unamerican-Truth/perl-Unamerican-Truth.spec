# $Id$
# Authority: dag
# Upstream: John Beppu <beppu$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unamerican-Truth

Summary: Perl module that implements srini's lost story
Name: perl-Unamerican-Truth
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unamerican-Truth/

Source: http://www.cpan.org/authors/id/B/BE/BEPPU/Unamerican-Truth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unamerican-Truth is a Perl module that implements srini's lost story.

This package contains the following Perl module:

    Unamerican::Truth

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Unamerican::Truth.3pm*
%dir %{perl_vendorlib}/Unamerican/
#%{perl_vendorlib}/Unamerican/Truth/
%{perl_vendorlib}/Unamerican/Truth.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Initial package. (using DAR)
