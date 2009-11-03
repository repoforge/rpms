# $Id$
# Authority: dries
# Upstream: John Siracusa <siracusa$mindspring,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Hotline

Summary: Hotline internet client
Name: perl-Net-Hotline
Version: 0.83
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Hotline/

Source: http://www.cpan.org/modules/by-module/Net/Net-Hotline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Net::Hotline modules implement a Hotline interface in Perl. Currently,
this includes only Net::Hotline::Client.  Hotline is an internet
client/server system that's sort of a cross between IRC and a traditional
BBS.  See http://www.hotlinesw.com/ for more information.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Hotline.p*
%{perl_vendorlib}/Net/Hotline
%{perl_vendorlib}/auto/Net/Hotline

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.83-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.83-1
- Initial package.
