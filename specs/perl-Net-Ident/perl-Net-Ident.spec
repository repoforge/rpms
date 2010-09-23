# $Id$
# Authority: dries
# Upstream: Jan-Pieter Cornet <johnpc$xs4all,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Ident

Summary: Lookup the username on the remote end of a TCP/IP connection
Name: perl-Net-Ident
Version: 1.23
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Ident/

#Source: http://www.cpan.org/modules/by-module/Net/Net-Ident-%{version}.tar.gz
Source: http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/Net-Ident-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Net::Ident is a module that looks up the username on the
remote side of a TCP/IP connection through the ident
(auth/tap) protocol described in RFC1413 (which supersedes
RFC931). Note that this requires the remote site to run a
daemon (often called identd) to provide the requested
information, so it is not always available for all TCP/IP
connections.

%prep
%setup -q -n %{real_name}-%{version}

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
%{perl_vendorlib}/Net/Ident.pm

%changelog
* Thu Sep 23 2010 David Hrbáč <david@hrbac.cz> - 1.23-1
- new upstream release

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
