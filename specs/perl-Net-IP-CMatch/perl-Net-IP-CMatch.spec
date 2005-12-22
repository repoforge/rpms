# $Id$
# Authority: dries
# Upstream: Beau E. Cox <beaucox$hawaii,rr,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-IP-CMatch

Summary: Efficiently match IP addresses against IP ranges with C
Name: perl-Net-IP-CMatch
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IP-CMatch/

Source: http://search.cpan.org/CPAN/authors/id/B/BE/BEAU/Net-IP-CMatch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Net::IP::CMatch is based upon, and does the same thing as
Net::IP::Match. The unconditionally exported subroutine 'match_ip'
determines if the ip to match ( first argument ) matches any of the
subsequent ip arguments. Match arguments may be absolute quads, as
'127.0.0.1', or contain mask bits as '111.245.76.248/29'. A true return
value indicates a match. It was written in C, rather than a macro,
preprocessed through Perl's source filter mechanism ( as is
Net::IP::Match ), so that the ip arguments could be traditional perl
scalars. The C code is lean and mean ( IMHO ).

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
%{perl_vendorarch}/Net/IP/CMatch.pm
%{perl_vendorarch}/auto/Net/IP/CMatch/

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
