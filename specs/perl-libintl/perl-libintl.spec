# $Id$

%define real_name libintl-perl

Summary: Internationalization library for Perl, compatible with gettext
Name: perl-libintl
Version: 1.11
Release: 2
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/libintl-perl/
Source: http://search.cpan.org/CPAN/authors/id/G/GU/GUIDO/libintl-perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl >= 2:5.8.0
Provides: perl-libintl-perl = %{version}-%{release}
Provides: perl(Locale::gettext_xs)
BuildArch: noarch

%description
The package libintl-perl is an internationalization library for Perl that
aims to be compatible with the Uniforum message translations system as
implemented for example in GNU gettext.


%prep
%setup -n libintl-perl-%{version}


%build
%{__perl} Makefile.PL \
    PREFIX="%{buildroot}%{_prefix}" \
    INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
# Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/lib*/perl5/*/*linux-thread-multi/
%{__rm} -f %{buildroot}%{_prefix}/lib*/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING* NEWS README THANKS TODO
%{_prefix}/lib/perl5/vendor_perl/*/Locale/
%{_mandir}/man?/*


%changelog
* Tue Nov  9 2004 Matthias Saou <http://freshrpms.net/> 1.11-2
- Fix : Added perl(Locale::gettext_xs) provides.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 1.11-1
- Initial RPM release.

