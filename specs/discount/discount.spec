# $Id$
# Authority: shuff
# Upstream: David Parsons <orc$pell,portland,or,us>

# update these when getting a new version
%define gitcommit gecf0b01
%define githash 9dabdb8

Summary: C compiler for Markdown
Name: discount
Version: 1.6.6
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.pell.portland.or.us/~orc/Code/discount/

Source: http://download.github.com/Orc-discount-v%{version}-0-%{gitcommit}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make

# we are a Markdown compiler
Provides: Markdown
Provides: /usr/bin/markdown
Provides: /usr/bin/mkd2html

%description
This is David Parsons' implementation of John Gruber's Markdown text to html
language.  There's not much here that differentiates it from any of the
existing Markdown implementations except that it's written in C instead of one
of the vast flock of scripting languages that are fighting it out for the Perl
crown.

Markdown provides a library that gives you formatting functions suitable for
marking down entire documents or lines of text, a command-line program that you
can use to mark down documents interactively or from a script, and a tiny (1
program so far) suite of example programs that show how to fully utilize the
markdown library.

discount also does, by default, various SmartyPants-style substitutions.


%package devel
Summary: Headers and development files for discount.
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}

%description devel
Install this package if you want to develop software that uses the Discount library.


%prep
%setup -n Orc-discount-%{githash}

%build
./configure.sh --prefix=%{_prefix} --confdir=%{_sysconfdir} --libdir=%{_libdir} --mandir=%{_mandir} --enable-dl-tag --enable-pandoc-header --enable-superscript --relaxed-emphasis
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_includedir}
%{__install} -d %{buildroot}%{_libdir}
%{__install} -d %{buildroot}%{_mandir}
%{__make} install.everything DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT INSTALL README VERSION
%doc %{_mandir}/man1/*
%doc %{_mandir}/man7/*
%{_bindir}/*
%{_libdir}/*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{_includedir}/*

%changelog
* Thu Aug 26 2010 Steve Huff <shuff@vecna.org> - 1.6.6-1
- Updated to version 1.6.6.
- Source moved to github.
- Why did I put theme in the devel package?

* Tue Mar 09 2010 Steve Huff <shuff@vecna.org> - 1.6.3-1
- Updated to version 1.6.3.

* Fri Feb 19 2010 Steve Huff <shuff@vecna.org> - 1.6.1-1
- Updated to version 1.6.1.

* Tue Oct 06 2009 Steve Huff <shuff@vecna.org> - 1.5.5-1
- Initial package.
