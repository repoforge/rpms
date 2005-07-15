# $Id$
# Authority: dag
# Upstream: Antonio Diaz Diaz <ant_diaz$teleline,es>

Summary: Data recovery tool
Name: ddrescue
Version: 1.0
Release: 1
License: GPL
Group: Applications/System
URL: http://www.gnu.org/software/ddrescue/ddrescue.html

Source: http://savannah.gnu.org/download/ddrescue/ddrescue-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
GNU ddrescue is a data recovery tool. It copies data from one file or block
device (hard disc, cdrom, etc) to another, trying hard to rescue data in
case of read errors.

Ddrescue does not truncate the output file if not asked to. So, every time
you run it on the same output file, it tries to fill in the gaps.

The basic operation of ddrescue is fully automatic. That is, you don't have
to wait for an error, stop the program, read the log, run it in reverse mode,
etc. 

%prep
%setup

%build
./configure \
	--prefix="%{_prefix}" \
	--datadir="%{_datadir}" \
	--infodir="%{_infodir}" \
	--mandir="%{_mandir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 ddrescue %{buildroot}%{_bindir}/ddrescue
%{__install} -Dp -m0644 doc/ddrescue.1 %{buildroot}%{_mandir}/man1/ddrescue.1
%{__install} -Dp -m0644 doc/ddrescue.info %{buildroot}%{_infodir}/ddrescue.info

%post
if [ -e %{_infodir}/ddrescue.info.gz ]; then
	/sbin/install-info %{_infodir}/ddrescue.info.gz %{_infodir}/dir
fi

%preun
if [ -e %{_infodir}/ddrescue.info.gz ]; then
	/sbin/install-info --delete %{_infodir}/ddrescue.info.gz %{_infodir}/dir
fi


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/ddrescue.1*
%doc %{_infodir}/ddrescue.info.*
%{_bindir}/ddrescue

%changelog
* Fri Jul 15 2005 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
