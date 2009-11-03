# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}
%{?rh7:%define _without_icu36 1}
%{?el2:%define _without_icu36 1}

Summary: Front end to diff for comparing files on a word per word basis
Name: dwdiff
Version: 1.5
Release: 1%{?dist}
License: OSL 2.0
Group: Applications/Text
URL: http://os.ghalkes.nl/dwdiff.html

Source: http://os.ghalkes.nl/dist/dwdiff-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
%{!?_without_icu36:BuildRequires: libicu-devel >= 3.6}
Requires: diffutils

%description
dwdiff is a front-end for the diff program that operates at the word level
instead of the line level. It is different from wdiff in that it allows the
user to specify what should be considered whitespace, and in that it takes an
optional list of characters that should be considered delimiters. Delimiters
are single characters that are treated as if they are words, even when there
is no whitespace separating them from preceding words or delimiters. 

%prep
%setup

%build
export CFLAGS="%{optflags}"
./configure \
    --prefix="%{buildroot}%{_prefix}" \
%{?_without_icu36:--without-unicode}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Move nl manpage
%{__install} -Dp -m0644 %{buildroot}%{_mandir}/nl.UTF-8/man1/dwdiff.1 %{buildroot}%{_mandir}/nl/man1/dwdiff.1

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_mandir}/nl.*/man1/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc Changelog COPYING README
%doc %{_mandir}/man1/dwdiff.1*
%lang(nl) %{_mandir}/nl/man1/dwdiff.1*
%{_bindir}/dwdiff

%changelog
* Tue Dec 02 2008 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Sun Jul 13 2008 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
