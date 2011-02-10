# $Id$
# Authority: dries
# Upstream: Peter Billam <peter,billam$pjb,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-Clui

Summary: The Command-Line User Interface
Name: perl-Term-Clui
Version: 1.64
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-Clui/

Source: http://search.cpan.org/CPAN/authors/id/P/PJ/PJB/Term-Clui-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Term::ReadKey)
Requires: perl(Term::ReadKey)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
Term::Clui offers a high-level user interface, with subroutines &choose
&ask &edit &view &confirm and &sorry. It works at a higher level than
widgets; it gives command-line applications a consistent "look and feel".
Its metaphor for the computer is a human-like conversation-partner,
and as each answer/response is completed it is summarised onto one line,
and remains on screen, so that the history of the dialogue gradually
accumulates on the screen and is available for review, or for cut/paste.
If &choose is called in an array context, it offers multiple choice.
Also included is the file-selector module Term::Clui::FileSelect,
with its main subroutine &select_file.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Term/Clui.pm
%{perl_vendorlib}/Term/Clui/*

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 1.64-1
- Updated to version 1.64.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.44-1
- Updated to version 1.44.

* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 1.43-1
- Updated to version 1.43.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.41-1
- Updated to version 1.41.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.40-1
- Updated to release 1.40.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.39-1
- Updated to release 1.39.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.37-1
- Updated to release 1.37.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.36-1
- Updated to release 1.36.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.35-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.35-1
- Updated to release 1.35.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Updated to release 1.30.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.29-1
- Updated to release 1.29.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Update to release 1.26.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Initial package.
