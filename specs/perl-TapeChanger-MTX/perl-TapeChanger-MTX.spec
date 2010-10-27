# $Id$
# Authority: dag
# Upstream: Tim Skirvin <tskirvin$killfile,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name TapeChanger-MTX

Summary: Perl module to use 'mtx' to manipulate a tape library
Name: perl-TapeChanger-MTX
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TapeChanger-MTX/

#Source: http://www.cpan.org/modules/by-module/TapeChanger/TapeChanger-MTX-%{version}.tar.gz
Source: http://search.cpan.org/CPAN/authors/id/T/TS/TSKIRVIN/TapeChanger-MTX-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: mt-st

%description
perl-TapeChanger-MTX is a Perl module to use use 'mtx' to manipulate a tape
library.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man1/tapechanger.1*
%doc %{_mandir}/man3/TapeChanger::MTX.3*
%dir %{perl_vendorlib}/TapeChanger/
#%{perl_vendorlib}/TapeChanger/MTX/
%{perl_vendorlib}/TapeChanger/MTX.pm
%{_bindir}/nexttape
%{_bindir}/tapechanger

%changelog
* Wed Oct 27 2010 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
