# $Id$

# Authority: dries
# Upstream: Ryan Eatmon <reatmon$mail,com>

%define real_name Net-XMPP
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: XMPP Perl Library
Name: perl-Net-XMPP
Version: 1.0
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-XMPP/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/Net-XMPP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The Extensible Messaging and Presence Protocol (XMPP) is an IETF standard
that provides a complete cross protocol messaging solution.  The problem
with current IM solutions is that they are all proprietary and cannot
talk to each other.  XMPP seeks to get rid of those barriers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/XMPP.pm
%{perl_vendorlib}/Net/XMPP
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.

