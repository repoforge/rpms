# $Id$

# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SNPP

Summary: Perl Simple Network Pager Protocol Client
Name: perl-Net-SNPP
Version: 1.17
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SNPP/

Source: http://www.cpan.org/modules/by-module/Net/Net-SNPP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Simple Network Pager Protocol Client.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net/SNPP.pm
%{perl_vendorlib}/Net/SNPP/

%changelog
* Mon Apr 10 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.16-1
- Initial package. (using DAR)
