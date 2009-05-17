# $Id$
# Authority: dag

Summary: Word-based diff front end
Name: wdiff
Version: 0.5
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.gnu.org/software/wdiff/wdiff.html

Source: http://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz
Patch: wdiff-0.5-debian-12.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: libtermcap-devel
BuildRequires: texinfo

%description
GNU wdiff is a front-end to GNU diff.  It compares two files, finding
which words have been deleted or added to the first in order to create
the second.  It has many output formats and interacts well with
terminals and pagers (notably with less).  GNU wdiff is particularly
useful when two texts differ only by a few words and paragraphs have
been refilled.

%prep
%setup
%patch -p1 -b .debian

%build
#autoreconf --force --install --symlink
./configure --prefix="%{_prefix}" --enable-cbars
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 cbars %{buildroot}%{_bindir}/cbars
%{__install} -Dp -m0755 wdiff %{buildroot}%{_bindir}/wdiff
%{__install} -Dp -m0644 wdiff.info %{buildroot}%{_infodir}/wdiff.info

%post
if [ -e %{_infodir}/wdiff.info.gz ]; then
    /sbin/install-info %{_infodir}/wdiff.info.gz %{_infodir}/dir
fi

%preun
if [ -e %{_infodir}/wdiff.info.gz ]; then
    /sbin/install-info --delete %{_infodir}/wdiff.info.gz %{_infodir}/dir
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BACKLOG ChangeLog COPYING NEWS README NEWS THANKS TODO
%doc %{_infodir}/wdiff.info*
%{_bindir}/cbars
%{_bindir}/wdiff

%changelog
* Mon Apr 27 2009 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
