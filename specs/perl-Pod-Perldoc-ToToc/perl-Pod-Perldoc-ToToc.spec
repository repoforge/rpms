# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Perldoc-ToToc

Summary: Translates Pod to a table of contents
Name: perl-Pod-Perldoc-ToToc
Version: 1.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Perldoc-ToToc/

Source: http://search.cpan.org//CPAN/authors/id/B/BD/BDFOY/Pod-Perldoc-ToToc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Translates Pod to a table of contents.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Pod/Perldoc/
%{perl_vendorlib}/Pod/Perldoc/ToToc.pm
%{perl_vendorlib}/Pod/TOC.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
