# $Id$
# Authority: dag
# Upstream: Chris Reinhardt <cpan$triv,org>

%{?dist: %{expand: %%define %dist 1}}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DNS

Summary: Net-DNS Perl module
Name: perl-Net-DNS
Version: 0.48
Release: 1
License: Artistic and GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/C/CR/CREIN/Net-DNS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503, perl(Digest::HMAC)
%{!?el2:BuildRequires: perl(Digest::MD5) >= 2.12, perl(MIME::Base64) >= 2.11}
%{?el2:BuildRequires: perl-Digest-MD5 >= 2.12, perl-MIME-Base64 >= 2.11}
Requires: perl >= 0:5.00503, perl(Digest::HMAC)
%{!?el2:Requires: perl(Digest::MD5) >= 2.12, perl(MIME::Base64) >= 2.11}
%{?el2:Requires: perl-Digest-MD5 >= 2.12, perl-MIME-Base64 >= 2.11}

%description
Net::DNS is a DNS resolver implemented in Perl.  It allows the
programmer to perform nearly any type of DNS query from a Perl
script.

%prep
%setup -n %{real_name}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" --no-online-tests \
        INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
        OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Remove this file because it generates an rpm dependency for Win32::Registry
%{__rm} -f %{buildroot}%{perl_vendorarch}/Net/DNS/Resolver/Win32.pm

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README TODO
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Net/
%{perl_vendorarch}/auto/Net/

%changelog
* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.48-1
- Update to release 0.48.

* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 0.47-1
- Updated to release 0.47.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.38-0
- Updated to release 0.38.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 0.33-0
- Initial package. (using DAR)
