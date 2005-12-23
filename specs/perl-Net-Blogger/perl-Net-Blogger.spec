# $Id$
# Authority: dries
# Upstream: Christopher H. Laco <claco$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Blogger

Summary: OOP-ish interface for accessing a weblog via the Blogger XML-RPC API
Name: perl-Net-Blogger
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Blogger/

Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLACO/Net-Blogger-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
Blogger.pm provides an OOP-ish interface for accessing a weblog via the
Blogger XML-RPC API.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Blogger.pm
%{perl_vendorlib}/Net/Blogger/

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
