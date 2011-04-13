# $Id$
# Authority: shuff
# Upstream: Eryq <eryq$zeegee,com>
# Upstream: David F. Skoll <dfs$roaringpenguin,com>
# Upstream: Dave O'Neill <dmo$roaringpenguin,com>
# ExcludeDist: el3

### EL6 ships with perl-MIME-tools-5.427-4.el6
%{?el6:# Tag: rfx}

### EL5 perl provides an older File::Temp
%{?el5:# Tag: rfx}
%{?el4:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-tools

Summary: Tools to manipulate MIME messages
Name: perl-MIME-tools
Version: 5.502
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-tools/

Source: http://search.cpan.org/CPAN/authors/id/D/DS/DSKOLL/MIME-tools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Path) >= 1
BuildRequires: perl(File::Spec) >= 0.6
BuildRequires: perl(File::Temp) >= 0.18
BuildRequires: perl(IO::File) >= 1.13
BuildRequires: perl(IO::Handle)
BuildRequires: perl(MIME::Base64) >= 3.03
BuildRequires: perl(Mail::Field) >= 1.05
BuildRequires: perl(Mail::Header) >= 1.01
BuildRequires: perl(Mail::Internet) >= 1.0203
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.8.0
BuildRequires: rpm-macros-rpmforge
Requires: perl(File::Path) >= 1
Requires: perl(File::Spec) >= 0.6
Requires: perl(File::Temp) >= 0.18
Requires: perl(IO::File) >= 1.13
Requires: perl(IO::Handle)
Requires: perl(MIME::Base64) >= 3.03
Requires: perl(Mail::Field) >= 1.05
Requires: perl(Mail::Header) >= 1.01
Requires: perl(Mail::Internet) >= 1.0203
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup


%description
MIME-tools - modules for parsing (and creating!) MIME entities Modules in this
toolkit : Abstract message holder (file, scalar, etc.), OO interface for
decoding MIME messages, an extracted and decoded MIME entity, Mail::Field
subclasses for parsing fields, a parsed MIME header (Mail::Header subclass),
parser and tool for building your own MIME parser, and utilities.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
#{__make} test 

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog INSTALLING MANIFEST META.yml README examples/
%doc %{_mandir}/man3/MIME::*.3pm*
%{perl_vendorlib}/MIME/

%changelog
* Wed Apr 13 2011 Steve Huff <shuff@vecna.org> - 5.502-2
- This package needs to be rfx; we need some dependencies we can't satisfy
  with stock el.
  Removed the test tag, this package has been in testing forever.
- Captured an outdated MIME::Base64 dependency.
- Removed a superfluous IO::Stringy dependency.

* Fri Mar 11 2011 David Hrbáč <david@hrbac.cz> - 5.502-1
- new upstream release

* Fri Feb 18 2011 David Hrbáč <david@hrbac.cz> - 5.501-1
- new upstream release

* Sun Jan 30 2011 David Hrbáč <david@hrbac.cz> - 5.500-1
- new upstream release

* Fri Sep 10 2010 David Hrbáč <david@hrbac.cz> - 5.428-1
- new upstream release

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 5.427-1
- Updated to release 5.427.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 5.426-1
- Updated to release 5.426.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 5.425-2
- Added dependency to perl(File::Temp) >= 0.17. (Christof Damian)

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 5.425-1
- Updated to release 5.425.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 5.420-2
- Disabled auto-requires for examples/.

* Mon Apr 17 2006 Dag Wieers <dag@wieers.com> - 5.420-1
- Updated to release 5.420.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 5.419-1
- Updated to release 5.419.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 5.418-2
- Rebuild.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 5.418-1
- Updated to release 5.418.

* Thu Mar 10 2005 Dag Wieers <dag@wieers.com> - 5.417-1
- Updated to release 5.417.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 5.415-1
- Updated to release 5.415.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
