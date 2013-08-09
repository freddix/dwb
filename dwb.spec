%define		gitver	9c32aec8661b894f429d41463114d68bb485376a

Summary:	A Webkit web browser
Name:		dwb
Version:	20130809
Release:	1
License:	GPL v3
Group:		X11/Applications
# git clone https://portix@bitbucket.org/portix/dwb.git
# git log -1 --format="%H" --> gitver
# git archive --format=tar --prefix=dwb-$(date +%Y%m%d)/ HEAD | xz -c > dwb-$(date +%Y%m%d)-$(git log -1 --format="%H").tar.xz
Source0:	%{name}-%{version}-%{gitver}.tar.xz
# Source0-md5:	ced373fc2135f3e50015d066327c02b1
BuildRequires:	gtk+-webkit-devel
BuildRequires:	libsoup-devel
Requires(post,postun):	desktop-file-utils
Requires:	glib-networking
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dwb is a lightweight web browser based on the webkit web browser
engine and the gtk toolkit. dwb is highly customizable and can be
easily configured through a web interface. It intends to be mostly
keyboard driven, inspired by firefox's vimperator plugin.

%prep
%setup -q

%build
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/dwb.desktop
%{_pixmapsdir}/dwb.png
%{_mandir}/man1/dwb.1*
%{_mandir}/man1/dwbem.1*
%{_mandir}/man1/dwbremote.1*
%{_mandir}/man7/dwb-js.7*

