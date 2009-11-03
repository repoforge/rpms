# $Id$
# Authority: dag
# Upstream: Matt J. Avitable <Matthew DOT Avitable AT gmail DOT com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Qmail-Envelope

Summary: Perl module to modify qmail envelope strings
Name: perl-Qmail-Envelope
Version: 0.53
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Qmail-Envelope/

Source: http://www.cpan.org/authors/id/M/MJ/MJA/Qmail-Envelope-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Qmail-Envelope is a Perl module to modify qmail envelope strings.

This package contains the following Perl module:

    Qmail::Envelope

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
%doc %{_mandir}/man3/Qmail::Envelope.3pm*
%dir %{perl_vendorlib}/Qmail/
%{perl_vendorlib}/Qmail/Envelope.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.53-1
- Initial package. (using DAR)
