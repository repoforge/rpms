# $Id$
# Authority: dries
# Upstream: Tom Wyant <wyant$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Astro-SpaceTrack

Summary: Downloads orbital elements from the Space Track web site
Name: perl-Astro-SpaceTrack
Version: 0.016
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Astro-SpaceTrack/

Source: http://search.cpan.org/CPAN/authors/id/W/WY/WYANT/Astro-SpaceTrack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This library logs in to the Space Track web site and downloads orbital
elements. It does nothing that you can't do with a web browser, but it
does give you a way to automate things.

Note that you are required to register for a username and password before
making use of the Space Track web site.

FEDERAL LAW FORBIDS THE REDISTRIBUTION OF DOWNLOADED ORBITAL ELEMENTS
TO THIRD PARTIES WITHOUT PRIOR PERMISSION.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL -y INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc %{_mandir}/man1/*
%{_bindir}/SpaceTrack
%{_bindir}/SpaceTrackTk
%{perl_vendorlib}/Astro/SpaceTrack.pm
%{perl_vendorlib}/Astro/SpaceTrack

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.016-1
- Updated to release 0.016.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.013-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.013-1
- Initial package.
