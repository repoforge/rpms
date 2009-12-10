# $Id$

# Authority: dries
# Upstream: Jeremy Muhlich <jmuhlich%20at%20bitflood,org>

%define real_name Net-IRC
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Perl interface to the Internet Relay Chat protocol
Name: perl-Net-IRC
Version: 0.76
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IRC/

Source: http://www.cpan.org/modules/by-module/Net/Net-IRC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(Socket)
BuildRequires: perl(Sys::Hostname)
Requires: perl(Carp)
Requires: perl(IO::File)
Requires: perl(IO::Select)
Requires: perl(IO::Socket)
Requires: perl(Socket)
Requires: perl(Sys::Hostname)

%filter_from_requires /^perl*/d
%filter_setup

%description
First intended to be a quick tool for writing an IRC script in Perl,
Net::IRC has grown into a comprehensive Perl implementation of the IRC
protocol (RFC 1459).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} -pi -e 's|IO::Socket::INET6?|IO::Socket::INET6|g;' *.pm
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
%{perl_vendorlib}/Net/IRC.pm
%{perl_vendorlib}/Net/IRC

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.76-1
- Updated to version 0.76.

* Tue Jul 26 2005 Jima <jima@devel.mintygreen.net> - 0.75-2
- IO::Socket::INET calls changed to IO::Socket::INET6 so IPV6 can be used.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 0.75-1
- Initial package.
