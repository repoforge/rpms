# $Id$
# Authority: dries
# Upstream: Jeff Zucker <jeff$vpservices,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AnyData

Summary: Easy access to data in many formats
Name: perl-AnyData
Version: 0.10
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AnyData/

Source: http://search.cpan.org/CPAN/authors/id/J/JZ/JZUCKER/AnyData-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
The AnyData modules provide simple and uniform access to data from
many sources -- perl arrays, local files, remote files retrievable via
http or ftp -- and in many formats including flat files (CSV, Fixed
Length, Tab Delimited, etc), standard format files (Web Logs,
Passwd files, etc.),  structured files (XML, HTML Tables) and binary
files with parseable headers (mp3s, jpgs, pngs, etc).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/AnyData.pm
%{perl_vendorlib}/AnyData

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
