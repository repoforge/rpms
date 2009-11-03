# $Id$
# Authority: dries
# Upstream: Douglas Wilson <dougw$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-FixedLength

Summary: Parse an ascii string containing fixed length fields into component parts
Name: perl-Parse-FixedLength
Version: 5.37
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-FixedLength/

Source: http://www.cpan.org/modules/by-module/Parse/Parse-FixedLength-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Parse an ascii string containing fixed length fields into component parts.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Parse/FixedLength.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 5.37-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 5.37-1
- Updated to release 5.37.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 5.35-1
- Updated to release 5.35.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 5.33-1
- Initial package.
