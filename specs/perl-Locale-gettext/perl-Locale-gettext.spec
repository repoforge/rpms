# $Id$
# Authority: dag

%define real_name gettext

Summary: Internationalization for Perl
Name: perl-Locale-gettext
Version: 1.01
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/gettext/

Source: http://www.cpan.org/modules/by-module/gettext/gettext-%{version}.tar.gz
Patch0: gettext-1.01-fix-example-in-README.patch
Patch1: gettext-1.01-includes.patch
Patch2: gettext-1.01-add-iconv.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software. 

It provides gettext(), dgettext(), dcgettext(), textdomain() and
bindtextdomain().

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1
%patch1 -p1 -b .includes
%patch2 -p0

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
        PREFIX="%{buildroot}%{_prefix}" \
        INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"
#%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.01-0
- Initial package. (using DAR)
