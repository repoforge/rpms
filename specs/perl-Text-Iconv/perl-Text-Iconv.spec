# $Id: perl-Text-Iconv 201 2004-06-03 15:24:49Z bert $

# Upstream: Michael Piotrowski <mxp@dynalabs.de>

# Authority: bert

Summary:	Text::Iconv perl module
Name:		perl-Text-Iconv
Version:	1.2
Release:	0
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Iconv-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root


%description
a Perl interface to the iconv() codeset conversion function, as 
defined by the Single UNIX Specification.

%prep
%setup -q -n Text-Iconv-%{version}

%build
#%{__perl} Makefile.PL
#%{__make} OPTIMIZE="%{rpmcflags}"
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
        PREFIX="%{buildroot}%{_prefix}" \
        INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT
%makeinstall
rm -f    %{buildroot}/usr/lib/perl5/5.8.3/i386-linux-thread-multi/perllocal.pod \
   %{buildroot}/usr/lib/perl5/vendor_perl/5.8.3/i386-linux-thread-multi/auto/Text/Iconv/.packlist


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_libdir}/perl5/vendor_perl/*/*/Text/Iconv.pm
%dir %{_libdir}/perl5/vendor_perl/*/*/auto/Text/Iconv
%{_libdir}/perl5/vendor_perl/*/*/auto/Text/Iconv/autosplit.ix
%{_libdir}/perl5/vendor_perl/*/*/auto/Text/Iconv/*.bs
%attr(755,root,root) %{_libdir}/perl5/vendor_perl/*/*/auto/Text/Iconv/*.so
%{_mandir}/man3/*

%changelog
* Tue Apr 06 2004 Bert de Bruijn <bert@debruijn.be>
- initial spec (adapted from PLD).

