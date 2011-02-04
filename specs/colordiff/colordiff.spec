# $Id$
# Authority: shuff
# Upstream: Dave Ewart <davee$sungate,co,uk>

Summary: a tool to colorize diff output
Name: colordiff
Version: 1.0.9
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://colordiff.sourceforge.net/

Source: http://colordiff.sourceforge.net/colordiff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: rpm-macros-rpmforge

%description
colordiff is a wrapper for 'diff' and produces the same output but with pretty
'syntax' highlighting. Colour schemes can be customized.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL_DIR="%{_bindir}" MAN_DIR="%{_mandir}/man1"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COPYING INSTALL README TODO colordiffrc-lightbg
%doc %{_mandir}/man?/*
%{_bindir}/*
%config %{_sysconfdir}/*

%changelog
* Fri Feb 04 2011 Steve Huff <shuff@vecna.org> - 1.0.9-1
- Initial package.
